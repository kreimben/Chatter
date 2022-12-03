import UserInfo from "@/utils/grpc/class/user_info";
import {chat_stub} from "@/utils/grpc/grpc.js";
import {ChatResponse} from "@/utils/grpc/class/chat";


const ListenChat = (req: ListenRequest, relay: (feature: ChatResponse) => void, error: (error: any) => void) => {
  const call = chat_stub.listenChat(req);

  call.on('data', function(feature: ChatResponse) {
    relay(feature);
  });
  call.on('end', function() {
    console.log(`ListenChat end`);
  });
  call.on('error', function(e: any) {
    error(e);
  });
  call.on('status', function(status: any) {
    console.log(`ListenChat status: ${status}`);
  });
}


class ListenRequest {
  me: UserInfo
  sender: UserInfo

  constructor(me: UserInfo, sender: UserInfo) {
    this.me = me
    this.sender = sender
  }
}

export {ListenChat, ListenRequest}
