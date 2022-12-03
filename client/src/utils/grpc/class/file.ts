
class File {
  content: any
  extension: string
  file_name: string

  constructor(content: any, extension: string, file_name: string) {
    this.content = content
    this.extension = extension
    this.file_name = file_name
  }
}

export default File;
