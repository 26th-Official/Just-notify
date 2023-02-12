from distutils.core import setup
setup(
  name = 'Just-Notify',       
  packages = ['Just-Notify'],  
  version = '0.1',     
  license='MIT',        
  description = 'Simple Package to notify when your program has finished Execution',  
  author = '26th_Official',                 
  author_email = '26thofficial.creator@gmail.com',      
  url = 'https://github.com/26th-Official/Just-notify',  
  download_url = 'https://github.com/26th-Official/Just-notify/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['NOTIFY', 'NOTIFICATION', 'FINISHED', 'EXECUTION', 'CODE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'plyer',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)