import UserInfo from "@/utils/grpc/class/user_info";
import {chat_stub} from "@/utils/grpc/grpc.js";


const GetUserList = (req: UserListQueryRequest, complete: (err: any, feature: UserListQueryResponse) => void) => {
  chat_stub.getUserList(req, function (err: any, feature: UserListQueryResponse) {
    complete(err, feature)
  })
}


class UserListQueryRequest {
  specific_user_name: string

  constructor(specific_user_name: string) {
    this.specific_user_name = specific_user_name
  }
}


class UserListQueryResponse {
  success: boolean
  users: UserInfo[]
  error_message?: string

  constructor(success: boolean, users: UserInfo[], error_message?: string) {
    this.success = success
    this.users = users
    this.error_message = error_message
  }
}


export {GetUserList, UserListQueryRequest, UserListQueryResponse}
