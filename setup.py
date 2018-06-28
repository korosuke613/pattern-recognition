from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

#ext_modules = [Extension('for_test', ['for_test.pyx'])]   #assign new.pyx module in setup.py.
#setup(name='for_test app',
#      cmdclass={'build_ext': build_ext},
#      ext_modules=ext_modules
#      )


ext_modules = [Extension('data_sets_cy', ['data_sets_cy.pyx'], language="c++")]   #assign new.pyx module in setup.py.
setup(name='data_sets_cy app',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules
)