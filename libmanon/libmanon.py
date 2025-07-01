try:
    from libset import libman
except Exception as e:
    print('Libman->Crashed')
    try:
        print()
        print('Calling fallback-mode: Librr')
        import getpass
        from libset.librr import log
        print('Unexpected crash of "libman"\n\t!!Unable to continue')
        log(f'"libman" crashed\n\tCaught Error: {e}', 'CriticlError')
        import os
        os.remove(os.path.join(os.path.pardir(__file__), libset, libman.py))
    except Exception as e:
        try:
            log('Broken Librr Final Response\n\tReturned: {e}', 'BrokenTrace')
        except:
            pass
        print()
        print('!!!!\tLibrr->Crashed')
        import os
        os.system('pip install git')
        import shutil
        shutil.rmtree(os.path.join(os.path.pardir(__file__), libset))
        try:
            os.removedirs(os.path.join(os.path.pardir(__file__), libset))
        except:
            pass
        os.system('git clone https://github.com/rish27c/libset.git')