import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

function init() {
  console.log(`init function!`)
  const PROTO_PATH = '../../chat.proto';
  console.log(`proto path: ${PROTO_PATH}`)
// Suggested options for similarity to existing grpc.load behavior
  const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true
    });
  console.log(`package definition: ${packageDefinition}`)
  const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
// The protoDescriptor object has the full package hierarchy
  const routeguide = protoDescriptor.routeguide;

  console.log(`before return: ${JSON.stringify(routeguide)}`)
  return new routeguide.RouteGuide('localhost:5000', grpc.credentials.createInsecure());
}

const chat_stub = init();

export {chat_stub}
