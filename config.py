BASE_AAS_URL = 'http://localhost:8000/submodels/aHR0cHM6Ly9hZG1pbi1zaGVsbC5pby9pZHRhL1N1Ym1vZGVsVGVtcGxhdGUvVGltZVNlcmllcy8xLzE/submodel-elements/'

VARIABLE_URLS = {
    "Time": f"{BASE_AAS_URL}Time",
    "sampleAccelerationX": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationX",
    "sampleAccelerationY": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationY",
    "sampleAccelerationZ": f"{BASE_AAS_URL}Metadata.Record.sampleAccelerationZ",
    "SamplingRate": f"{BASE_AAS_URL}Segments.LinkedSegment.SamplingRate"
}
