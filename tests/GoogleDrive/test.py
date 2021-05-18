from Drive.GoogleDrive import GoogleAPI

def main():
    service = GoogleAPI('credentials.json', 'token.pickle')
    service.download_folder_content('folder_name')

if __name__ == '__main__':
    main()