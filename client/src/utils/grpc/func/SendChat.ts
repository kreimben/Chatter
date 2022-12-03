import {ChatRequest} from "@/utils/grpc/class/chat";
import {chat_stub} from "@/utils/grpc/grpc.js";

const SendChat = (req: ChatRequest) => {
  chat_stub.sendChat(req, function (err: any, feature: any) {
    if (err) {
      console.error(err)
    }
  })
}

export default SendChat
