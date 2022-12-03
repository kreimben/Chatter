import {ConnectServer, ConnectServerReqeust, ConnectServerResponse} from "@/utils/grpc/func/ConnectServer";

const register = (user_name: string) => {
  console.log(`event: ${JSON.stringify(event)}`)
  const req = new ConnectServerReqeust(user_name);

  ConnectServer(req, function (err: any, feature: ConnectServerResponse) {
    if (err) {
      console.error(err)
    } else {
      console.log(feature.success)
    }
  });
}


export {register}
