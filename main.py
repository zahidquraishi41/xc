from argparse import ArgumentParser
from db_manager import DBManager
import pyperclip


class App:
    def __init__(self) -> None:
        self.dbm = DBManager()

    def copy_to_cb(self, title: str):
        text = self.dbm.get(title)
        if text:
            pyperclip.copy(text)
            print('Copied to clipboard')
        else:
            print(f'{title} isn\'t saved.')

    def save_text(self, title: str, text: str = None):
        self.dbm.set(title, ' '.join(text))
        print('Saved successfully')

    def delete_entry(self, title: str):
        if self.dbm.remove(title):
            print('Removed successfully.')
        else:
            print(f'Title "{title}" not found')

    def list_saved_data(self):
        data = self.dbm.get_all()
        max_key_length = max(len(key) for key in data.keys())
        if not data:
            print('No data is saved!')
            return
        print(f"{'Title':<{max_key_length + 4}}Text")
        for k, v in data.items():
            print(f"{k:<{max_key_length + 4}}{v}")


def main():
    parser = ArgumentParser(description='Manage and copy text data by title.')
    parser.add_argument('title', nargs='?',
                        help='Title of the text data to be copied.')
    parser.add_argument('text', nargs='...',
                        help='Text data to be saved (optional, used when saving text to the database).')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all saved titles and texts')
    parser.add_argument('-d', '--delete',
                        help='Delete saved entry with the specified title')

    args = parser.parse_args()
    app = App()
    try:
        if args.list:
            app.list_saved_data()
        elif args.delete:
            app.delete_entry(args.delete)
        elif args.title:
            if args.text:
                app.save_text(args.title, args.text)
            else:
                app.copy_to_cb(args.title)
        else:
            print('Invalid command. Use "xc -h" to see available commands.')
    except Exception as e:
        print('An error occured!')
        print(e)


if __name__ == '__main__':
    main()
