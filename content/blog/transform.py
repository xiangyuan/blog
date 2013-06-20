import os
import shutil

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('rst'):
            src = '%s/%s' % (root, f)
            dst = '%s-%s' % (root, f)
            shutil.move(src, dst)
            print 'Moved %s to %s' % (src, dst)
