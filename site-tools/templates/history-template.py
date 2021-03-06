from boost_site.util import htmlencode

title = 'Boost Version History'
entries = pages.match_pages(['feed/history/*.qbk|released'])

for entry in entries:
    emit('\n')
    emit('              <h2 class="news-title">\n              <a name="i%s" id="i%s"></a><a href="/%s">%s</a></h2>\n\n' % (entry.id, entry.id, htmlencode(entry.location), entry.title_xml))
    emit('              <p class="news-date">%s</p>\n\n' % (entry.web_date()))
    emit('              <div class="news-description">\n')
    emit('                <span class="brief"><span class="purpose">%s</span></span>\n' % (entry.purpose_xml))
    emit('              </div>\n\n')
    emit('<ul class="menu">\n')
    emit('<li>')
    emit('<a href="/%s">Release Notes</a>' % htmlencode(entry.location))
    emit('</li>\n')
    if(entry.download_item):
        emit('<li>')
        emit('<a href="%s">Download</a>' % htmlencode(entry.download_item))
        emit('</li>\n')
    if(entry.documentation):
        emit('<li>')
        emit('<a href="%s">Documentation</a>' % htmlencode(entry.documentation))
        emit('</li>\n')
    emit('</ul>\n')
