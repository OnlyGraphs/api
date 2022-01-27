# Generate the Protocol Buffers and the GRPC Stubs for all of the protofiles
# Note: This requires `grpcio-tools` to be installed locally, this can be done throught pip
python3 -m grpc_tools.protoc -I ./../proto \
        --python_out=. \
        --grpc_python_out=. \
        ./../proto/*.proto
