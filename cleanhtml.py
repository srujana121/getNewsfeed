import re
def cleanhtmltags(raw_html):
    """
    Convert raw html code to text by removing all tags.
    """
    cleanr =re.compile('<.*?>')
    withouttags = re.sub(cleanr,'', raw_html)
    withouttags.split()
    without_mult_spaces= ' '.join(withouttags.split())
    return without_mult_spaces
