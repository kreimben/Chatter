import UserInfo from "@/utils/grpc/class/user_info";
import {chat_stub} from "@/utils/grpc/grpc.js";
import {ChatRequest} from "@/utils/grpc/class/chat";

const GetAllChats = (req: ListenRequest, complete: (err: any, feature: GetAllChatsResponse) => void) => {
  chat_stub.getAllChats(req, function (err: any, feature: GetAllChatsResponse) {
    complete(err, feature)
  })
}


class ListenRequest {
  me: UserInfo
  sender: UserInfo

  constructor(me: UserInfo, sender: UserInfo) {
    this.me = me
    this.sender = sender
  }
}


class GetAllChatsResponse {
  chats: ChatRequest[]

  constructor(chats: ChatRequest[]) {
    this.chats = chats
  }
}

export {GetAllChats, ListenRequest, GetAllChatsResponse}
