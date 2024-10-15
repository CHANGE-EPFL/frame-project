from aiobotocore.session import get_session
from io import BytesIO
from fastapi.logger import logger
from fastapi.exceptions import HTTPException
from typing import Tuple
from PIL import Image
from api.config import config
from api.utils.mimetype import image_mimetypes
from fastapi.datastructures import UploadFile
import os
import urllib.parse
import mimetypes


class S3Client(object):

    def __init__(self, s3_endpoint_url, s3_access_key_id, s3_secret_access_key, region, *args,
                 **kwargs):
        self.s3_endpoint_url = s3_endpoint_url
        self.s3_access_key_id = s3_access_key_id
        self.s3_secret_access_key = s3_secret_access_key
        self.region = region

    async def path_exists(self, file_path: str):
        """Check if file exists in S3 storage

        Args:
            file_path (str): Path of the file in S3

        Returns:
            bool: True if file exists, False otherwise
        """
        key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            key = f"{config.S3_PATH_PREFIX}{file_path}"

        # check if file_path exists
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            try:
                response = await client.head_object(
                    Bucket=config.S3_BUCKET, Key=key)
                if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    return True
            except Exception as e:
                return False
        return False

    async def get_file(self, file_path: str):
        """Extract file content and mimetype from S3 storage

        Args:
            file_path (str): Path of the file in S3

        Returns:
            Tuple: File content and mimetype
        """
        key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            key = f"{config.S3_PATH_PREFIX}{file_path}"

        # get file from file path
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            try:
                response = await client.get_object(
                    Bucket=config.S3_BUCKET, Key=key)
                if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    # Read the content of the S3 object
                    file_content = await response['Body'].read()
                    return file_content, response["ContentType"]
            except Exception as e:
                return False, False
        return False, False

    async def upload_local_file(self, parent_path, file_path: str, s3_folder: str = ""):
        """Upload local file to S3 storage

        Args:
            parent_path (str): Parent path of the file
            file_path (str): Path to local file relative to parent path
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Returns:
            dict: S3 upload reference
        """

        content_type = self._get_mime_type(file_path)
        if content_type in image_mimetypes:
            return await self._upload_local_image(parent_path, file_path, s3_folder)
        return await self._upload_local_file(parent_path, file_path, s3_folder)

    async def upload_file(self, upload_file: UploadFile, s3_folder: str = ""):
        """Upload file to S3 storage

        Args:
            upload_file (UploadFile): UploadFile object
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Returns:
            dict: S3 upload reference
        """
        # if mimetype is image upload image
        if upload_file.content_type in image_mimetypes:
            return await self._upload_image(upload_file, s3_folder)
        return await self._upload_file(upload_file, s3_folder)

    async def move_file(self, file_path: str, destination_path: str):
        """Move a file from one location to another in the same S3 storage

        Args:
            file_path (str): Path of the file in S3
            destination_path (str): Destination path in S3

        Returns:
            Any: File path if deleted, False otherwise
        """
        source_key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            source_key = f"{config.S3_PATH_PREFIX}{file_path}"

        destination_key = destination_path
        if not destination_path.startswith(config.S3_PATH_PREFIX):
            destination_key = f"{config.S3_PATH_PREFIX}{destination_path}"

        # copy to new location and delete source
        res = await self.copy_file(source_key, destination_key)
        if res is not False:
            await self.delete_file(source_key)
        return res

    async def copy_file(self, file_path: str, destination_path: str):
        """Copy a file from one location to another in the same S3 storage

        Args:
            file_path (str): Path of the file in S3
            destination_path (str): Destination path in S3

        Returns:
            Any: File path if deleted, False otherwise
        """
        source_key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            source_key = f"{config.S3_PATH_PREFIX}{file_path}"

        destination_key = destination_path
        if not destination_path.startswith(config.S3_PATH_PREFIX):
            destination_key = f"{config.S3_PATH_PREFIX}{destination_path}"

        # copy file_path to new location
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            response = await client.copy_object(
                Bucket=config.S3_BUCKET,
                CopySource={'Bucket': config.S3_BUCKET, 'Key': source_key},
                Key=destination_key)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                logger.info(
                    f"File copied path : {self.s3_endpoint_url}/{config.S3_BUCKET}/{destination_key}")
                return destination_key
        return False

    async def delete_file(self, file_path: str):
        """Delete file from S3 storage

        Args:
            file_path (str): Path of the file in S3

        Returns:
            Any: File path if deleted, False otherwise
        """
        key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            key = f"{config.S3_PATH_PREFIX}{file_path}"

        # delete file_path
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            response = await client.delete_object(
                Bucket=config.S3_BUCKET, Key=key)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 204:
                logger.info(
                    f"File deleted path : {self.s3_endpoint_url}/{config.S3_BUCKET}/{key}")
                return key
        return False

    async def delete_files(self, file_path: str):
        """Delete files recursively from S3 storage

        Args:
            file_path (str): Path of the file in S3

        Returns:
            Any: File path if deleted, False otherwise
        """
        folder_key = file_path
        if not file_path.startswith(config.S3_PATH_PREFIX):
            folder_key = f"{config.S3_PATH_PREFIX}{file_path}"

        # delete file_path
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            # delete content, if any
            paginator = client.get_paginator('list_objects_v2')
            async for result in paginator.paginate(Bucket=config.S3_BUCKET, Prefix=folder_key):
                for content in result.get('Contents', []):
                    object_key = content['Key']
                    response = await client.delete_object(Bucket=config.S3_BUCKET, Key=object_key)
                    if response["ResponseMetadata"]["HTTPStatusCode"] == 204:
                        logger.info(
                            f"File deleted path : {self.s3_endpoint_url}/{config.S3_BUCKET}/{object_key}")

            # delete object
            response = await client.delete_object(Bucket=config.S3_BUCKET, Key=folder_key)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 204:
                logger.info(
                    f"File deleted path : {self.s3_endpoint_url}/{config.S3_BUCKET}/{folder_key}")
                return folder_key
        return False

    #
    # Private methods
    #

    async def _convert_image(self, upload_file: UploadFile) -> Tuple[BytesIO, BytesIO]:
        """Convert an image to webp format

        Args:
            upload_file (UploadFile): UploadFile object

        Returns:
            Tuple[BytesIO, BytesIO]: Data of webp image and data of original image
        """
        request_object_content = await upload_file.read()
        origin_BytesIo = BytesIO(request_object_content)
        image = Image.open(origin_BytesIo)
        data = BytesIO()
        image.save(data, format="webp", quality=60)
        return (data, origin_BytesIo)

    async def _get_unique_filename(self,
                                   filename: str,
                                   ext: str = "",
                                   s3_folder: str = "") -> Tuple[str, str]:
        """Get unique file path in S3 and file name, change extension if one is provided

        Args:
            filename (str): File name
            ext (str, optional): New file extension. Defaults to "".
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Returns:
            Tuple[str, str]: File path in S3 and new or original file name
        """
        split_file_name = os.path.splitext(filename)
        ext = ext if ext != "" else split_file_name[1]
        name = split_file_name[0]
        return (f"{s3_folder}/{name}{ext}", f"{name}{ext}")

    async def _upload_image(self, upload_file: UploadFile, s3_folder: str = ""):
        """Upload image to S3, convert to webp if necessary

        Args:
            upload_file (UploadFile): UploadFile object
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Raises:
            HTTPException: When S3 upload fails

        Returns:
            dict: S3 upload reference
        """
        if upload_file.content_type == "image/webp":
            # no need to convert to webp
            return self._upload_file(upload_file, s3_folder)
        else:
            # convert to bytes
            (data, origin_data) = await self._convert_image(upload_file)

            # Webp converted image
            mimetype = "image/webp"
            (unique_file_name, name) = await self._get_unique_filename(upload_file.filename, ".webp", s3_folder=s3_folder)

            key = f"{config.S3_PATH_PREFIX}{unique_file_name}"
            uploads3 = await self._upload_fileobj(bucket=config.S3_BUCKET,
                                                  key=key,
                                                  data=data.getvalue(),
                                                  mimetype=mimetype)

            if not uploads3:
                raise HTTPException(status_code=500,
                                    detail="Failed to upload image to S3")

            # Original image
            (unique_alt_file_name, alt_name) = await self._get_unique_filename(upload_file.filename, s3_folder=s3_folder)
            alt_key = f"{config.S3_PATH_PREFIX}{unique_alt_file_name}"
            alt_uploads3 = await self._upload_fileobj(
                bucket=config.S3_BUCKET,
                key=alt_key,
                data=origin_data.getvalue(),
                mimetype=upload_file.content_type)

            if not alt_uploads3:
                raise HTTPException(status_code=500,
                                    detail="Failed to upload image to S3")

            # response http to be used by the frontend
            return {
                "path": urllib.parse.quote(key),
                "name": name,
                "size": uploads3,
                "alt_path": urllib.parse.quote(alt_key),
                "alt_name": alt_name,
                "alt_size": alt_uploads3
            }

    async def _upload_file(self, upload_file: UploadFile, s3_folder: str = "") -> dict:
        """Upload file to S3, as is

        Args:
            upload_file (UploadFile): UploadFile object
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Raises:
            HTTPException: When S3 upload fails

        Returns:
            dict: S3 upload reference
        """
        (filename, name) = await self._get_unique_filename(upload_file.filename, s3_folder=s3_folder)
        key = f"{config.S3_PATH_PREFIX}{filename}"
        uploads3 = await self._upload_fileobj(bucket=config.S3_BUCKET,
                                              key=key,
                                              data=upload_file.file._file,
                                              mimetype=upload_file.content_type)
        if uploads3:
            # response http to be used by the frontend
            return {
                "path": urllib.parse.quote(key),
                "name": name,
                "size": uploads3
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to upload file to S3")

    async def _upload_local_image(self, parent_path, file_path: str, s3_folder: str = "") -> dict:
        """Upload local image to S3, convert to webp if necessary

        Args:
            parent_path (str): Parent path of the file
            file_path (str): Path to local file relative to parent path
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Raises:
            HTTPException: When S3 upload fails

        Returns:
            dict: S3 upload reference
        """
        if file_path.endswith(".webp"):
            # no need to convert to webp
            return await self._upload_local_file(parent_path, file_path, s3_folder)
        else:
            alt_info = None
            try:
                # convert to webp
                file_path_alt = self._convert_image_file(
                    parent_path, file_path)

                # upload converted file
                alt_info = await self._upload_local_file(
                    parent_path, file_path_alt, s3_folder)
            except Exception as e:
                logger.error(e)

            # Original file
            orig_info = await self._upload_local_file(
                parent_path, file_path, s3_folder)

            # response http to be used by the frontend
            return {
                "path": orig_info["path"],
                "name": orig_info["name"],
                "size": orig_info["size"],
                "alt_path": alt_info["path"],
                "alt_name": alt_info["name"],
                "alt_size": alt_info["size"]
            } if alt_info else orig_info

    def _convert_image_file(self, parent_path: str, file_path: str) -> str:
        split_file_path = os.path.splitext(file_path)
        file_path_webp = f"{split_file_path[0]}.webp"
        input_file = os.path.join(parent_path, file_path)
        output_file = os.path.join(parent_path, file_path_webp)

        Image.open(input_file).save(output_file, format="webp", quality=60)

        return file_path_webp

    async def _upload_local_file(self, parent_path, file_path: str, s3_folder: str = "") -> dict:
        """Upload file to S3, as is

        Args:
            parent_path (str): Parent path of the file
            file_path (str): Path to local file relative to parent path
            s3_folder (str, optional): Relative parent folder in S3. Defaults to "".

        Raises:
            HTTPException: When S3 upload fails

        Returns:
            dict: S3 upload reference
        """

        (filename, name) = await self._get_unique_filename(file_path, s3_folder=s3_folder)
        key = f"{config.S3_PATH_PREFIX}{filename}"
        with open(os.path.join(parent_path, file_path), 'rb') as file:
            uploads3 = await self._upload_fileobj(bucket=config.S3_BUCKET,
                                                  key=key,
                                                  data=file,
                                                  mimetype=self._get_mime_type(file_path))
        if uploads3:
            # response http to be used by the frontend
            return {
                "path": urllib.parse.quote(key),
                "name": name,
                "size": uploads3
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to upload file to S3")

    async def _upload_fileobj(self, data: BytesIO, bucket: str, key: str, mimetype: str) -> bool:
        """Perform the data upload to S3

        Args:
            data (BytesIO): Data to be uploaded
            bucket (str): Destination bucket
            key (str): Path of the obejct in the bucket
            mimetype (str): Object mimetype

        Returns:
            bool: True if upload was successful, the object size in bytes otherwise
        """
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                endpoint_url=self.s3_endpoint_url,
                aws_secret_access_key=self.s3_secret_access_key,
                aws_access_key_id=self.s3_access_key_id) as client:
            resp = await client.put_object(
                Bucket=bucket,
                Key=key,
                Body=data,
                ACL="public-read",
                ContentType=mimetype)

            if resp["ResponseMetadata"][
                    "HTTPStatusCode"] == 200:
                logger.info(
                    f"File uploaded path : {self.s3_endpoint_url}/{bucket}/{key}")
                resp = await client.head_object(Bucket=bucket, Key=key)
                object_size = resp.get("ContentLength", 0)
                return object_size
        return False

    def _get_mime_type(self, file_name):
        mime_type, encoding = mimetypes.guess_type(file_name)
        if mime_type is None:
            if file_name.endswith('.webp'):
                mime_type = 'image/webp'
            else:
                mime_type = 'application/octet-stream'
        return mime_type


s3_client = S3Client(config.S3_ENDPOINT_PROTOCOL + config.S3_ENDPOINT_HOSTNAME,
                     config.S3_ACCESS_KEY_ID,
                     config.S3_SECRET_ACCESS_KEY, config.S3_REGION)
