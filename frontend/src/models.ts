export interface Reference {
  citation: string;
  doi: string;
}

export interface Measures {
  name: string;
  description?: string;
  datasets?: string[];
}

export interface Instrument {
  name: string;
  description?: string;
  measures: Measures[];
}

export interface Track {
  file: string;
  columns: {
    latitude: string;
    longitude: string;
    timestamp: string;
  },
  color?: string;
  timestamp_format?: string;
}

export interface Campaign {
  name: string;
  acronym: string;
  type?: string;
  color?: string;
  objectives?: string;
  start_date?: string;
  end_date?: string;
  location?: string;
  platform?: string;
  start_location: [number, number];
  end_location?: [number, number];
  images?: string[];
  track?: Track;
  fundings: string[];
  references: Reference[];
  instruments: Instrument[];
}

export interface CampaignStore {
  campaigns: string[];
}