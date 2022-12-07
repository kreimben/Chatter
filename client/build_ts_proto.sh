echo `npx grpc_tools_node_protoc \
    --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
    --ts_out=grpc_js:./src/proto \
    -I.. \
    ../*.proto`


#echo `yarn run grpc_tools_node_protoc \
#    --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
#    --ts_out=./src/proto \
#    -I.. \
#    ../chat.proto`
