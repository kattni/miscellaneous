"""Requires slugify."""
#!/usr/bin/env python
import sys
from datetime import datetime
from subprocess import call
from slugify import slugify
from post_template import TEMPLATE


def make_entry(title, tags):
    today = datetime.today()
    slug = slugify(title)
    file_create = "/Path/to/your/site/content/{}/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.year, today.month, today.day, slug)
    template = TEMPLATE.strip().format(title=title,
                                       year=today.year,
                                       month=today.month,
                                       day=today.day,
                                       hour=today.hour,
                                       minute=today.minute,
                                       tags=tags,
                                       slug=slug)
    with open(file_create, "w") as w:
        w.write(template)
    print("File created -> " + file_create)
    call(["pycharm", file_create])  # Opens PyCharm. Update to your editor.


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_entry(sys.argv[1], sys.argv[2])
    else:
        print("No title given")
