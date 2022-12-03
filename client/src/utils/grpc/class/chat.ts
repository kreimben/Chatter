import UserInfo from "@/utils/grpc/class/user_info";

class ChatRequest {
  sender: UserInfo
  message?: string
  file?: File
  target: UserInfo

  constructor(sender: UserInfo, target: UserInfo, message?: string, file?: File) {
    this.sender = sender
    this.message = message
    this.file = file
    this.target = target
  }
}

class ChatResponse {
  success: boolean
  chat_req?: ChatRequest
  error_message?: string

  constructor(success: boolean, chat_req?: ChatRequest, error_message?: string) {
    this.success = success
    this.chat_req = chat_req
    this.error_message = error_message
  }
}


export {ChatResponse, ChatRequest};
