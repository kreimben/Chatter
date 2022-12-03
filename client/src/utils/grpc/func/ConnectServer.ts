import {chat_stub} from "@/utils/grpc/grpc.js";
import UserInfo from "@/utils/grpc/class/user_info";


const ConnectServer = (req: ConnectServerReqeust, complete: (err: any, feature: ConnectServerResponse) => void) => {
  chat_stub.connectServer(req, function (err: any, feature: ConnectServerResponse) {
    complete(err, feature)
  })
}

class ConnectServerReqeust {
  user_name: string

  constructor(user_name: string) {
    this.user_name = user_name;
  }
}

class ConnectServerResponse {
  success: boolean
  user?: UserInfo
  error_message?: string

  constructor(success: boolean, user?: UserInfo, error_message?: string) {
    this.success = success;
    if (user !== null) {
      this.user = user;
    } else {
      this.error_message = error_message;
    }
  }
}


export {ConnectServer, ConnectServerReqeust, ConnectServerResponse}
