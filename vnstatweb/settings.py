debug = False

bgcolor = 'white'
template = {
    'graphs': (
        {
            'interface': 'em0',
        },
    ),
    'bgcolor': bgcolor,
    'cssbody': 'body { background-color: %s; }' % bgcolor,
}

vnstati_cmd = '/usr/local/bin/vnstati'
img_directory = '/var/www/vnstat_images'
socket = '/var/www/vnstat.sock'

cachetime = 15
