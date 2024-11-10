from setuptools import setup, find_packages

setup(
    name='TurboTask',
    packages=find_packages(),
    version='1.0',
    description='Makes Handling files easier.',
    # description='Download shit and youtube playlists without having to enter any API keys!',
    long_description="A Utilities to speed up tasks.",
    # long_description_content_type='text/markdown',
    author='Fabian',
    author_email='fabianjoseph063@gmail.com',
    url='https://github.com/Fector101/TurboTask/',
    entry_points={
        'console_scripts': [
            'create = TurboTask.main:create',  # 'command_name = package.module:function'
            'durate = TurboTask.main:cal_files_duration',  # 'command_name = package.module:function'
            'group = TurboTask.main:sort',  # 'command_name = package.module:function'
            'groupShow = TurboTask.main:sortSeason',  # 'command_name = package.module:function'
            'del = TurboTask.main:delEmptyAll',  # 'command_name = package.module:function'
            'create_dir = TurboTask.main:create_with_specified_dir_',
            'TurboTask = TurboTask.main:main_',

        ]
    }
)
