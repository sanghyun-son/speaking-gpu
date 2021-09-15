import setuptools

def main() -> None:
    setuptools.setup(
        name='speaking_gpu',
        version='1.0',
        url='https://sanghyun-son.github.i/',
        license='MIT',
        author='Sanghyun Son',
        author_email='sonsang35@gmail.com',
        description='Speaking GPU interface',
        packages=setuptools.find_packages('core'),
        install_requires=[
            'discord.py',
        ]
    )
    return

if __name__ == '__main__':
    main()