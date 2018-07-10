from cx_Freeze import setup, Executable

"""
Настройки для сборки исполняемого файла в windows
"""

executables = [Executable('book_titles.py')]

includes = ['pkg_resources', 'scrapy', 'cffi', 'idnadata']

zip_include_packages = ['pkg_resources']

options = {
    'build_exe': {
        'includes': includes,
        'packages': ['pkg_resources', 'scrapy', 'idna', 'email'],
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows'
    }
}

setup(
    name='book_titles',
    version='0.0.1',
    description='Парсер названий книг с сайта http://books.toscrape.com',
    executables=executables,
    options=options)
