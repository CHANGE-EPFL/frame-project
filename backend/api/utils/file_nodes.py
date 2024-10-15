from urllib.parse import quote


class FileNode:
    """A node in a tree representing a file system, used to represent a list of file objects in S3
    """

    def __init__(self, name, path=None, size=None, is_file=False, alt_name=None, alt_path=None, alt_size=None, children=[]):
        self.name = name
        self.path = path
        self.size = size
        self.alt_name = None
        self.alt_path = None
        self.alt_size = None
        self.is_file = is_file
        self.children = children if not is_file else None

    def add_file(self, file_ref):
        """Add a file to the tree

        Args:
            file_ref (Dict): A dictionary representing a file object in S3
        """
        current_node = self
        parts = file_ref["name"].split('/')
        current_parts = []

        for part in parts:
            current_parts.append(part)
            matching_child = next(
                (child for child in current_node.children if child.name == part), None)

            if matching_child is None:
                is_file = True if part == parts[-1] else False
                new_path = file_ref["path"] if is_file else quote("/".join(
                    current_parts), safe="/")
                if not is_file:
                    new_path = file_ref["path"].split(new_path)[0] + new_path
                new_size = file_ref["size"] if is_file else None
                new_node = FileNode(part, new_path, new_size, is_file)
                if is_file and "alt_name" in file_ref:
                    new_node.alt_name = file_ref["alt_name"]
                    new_node.alt_path = file_ref["alt_path"]
                    new_node.alt_size = file_ref["alt_size"]
                current_node.children.append(new_node)
                current_node = new_node
            else:
                current_node = matching_child

    def to_dict(self):
        rval = {
            "name": self.name,
            "path": self.path,
            "is_file": self.is_file,
            "children": [child.to_dict() for child in self.children] if self.children else None
        }
        if self.is_file:
            rval["size"] = self.size
            del rval["children"]
        if self.alt_name is not None:
            rval["alt_name"] = self.alt_name
            rval["alt_path"] = self.alt_path
            rval["alt_size"] = self.alt_size
        return rval
