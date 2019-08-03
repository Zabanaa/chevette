# step 1
# retrieve all entries inside /entries and parse them as markdown
# convert each one to html and save them to a different location.
import os
import misaka

BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, 'entries')
OUTPUT_DIR = os.path.join(BASE_DIR, 'public')


def get_all_entries():

    fs = (
            f for f in os.listdir(CONTENT_DIR)
            if os.path.isfile(os.path.join(CONTENT_DIR, f))
            and f.endswith('.md')
            and not f.startswith('.')
        )
    return fs


def generate_html_from_markdown(files):

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for file in files:
        with open(os.path.join(CONTENT_DIR, file), 'r') as f:
            content = misaka.html(f.read())
            print(content)


entries = get_all_entries()
generate_html_from_markdown(entries)