import copy
import subprocess
from collections import namedtuple
from vnstatweb import app, settings
from flask import send_from_directory, render_template


def getbasedata():
    data = copy.deepcopy(settings.template)
    data['name'] = 'vnstatweb.py'
    return data


Image = namedtuple('Image', ['directory', 'file', 'fullpath'])
def fname(i, t):
    return Image(settings.img_directory, "%s-%s.png" % (i, t), '%s/%s-%s.png' % (settings.img_directory, i, t))


def generate_image(interface, filename, param):
    cmd = "{0} -i {1} -c {2} {3} -o {4}".format(settings.vnstati_cmd, interface, 
              settings.cachetime, param, filename)
    app.logger.debug("Calling: %s", cmd)
    subprocess.check_call(cmd.split())


def sanity_check_iface(i):
    if i not in [x['interface'] for x in settings.template['graphs']]:
        raise Exception("Invalid interface")


def sanity_check_term(t):
    if t not in "summary hours days months top10".split():
        raise Exception("Invalid term")


@app.route('/')
def index():
    data = getbasedata()
    return render_template('index.j2', **data)


@app.route('/viewimage/<string:iface>')
def viewimage(iface):
    sanity_check_iface(iface)
    data = getbasedata()
    data['interface'] = iface
    return render_template('image.j2', **data)


@app.route('/render/<string:iface>/<string:term>')
def render(iface, term):
    sanity_check_iface(iface)
    sanity_check_term(term)
    i = fname(iface, term)
    generate_image(iface, i.fullpath, "--%s" % term)
    return send_from_directory(i.directory, i.file,
                               cache_timeout=settings.cachetime * 60)
