import os
import sys

def finish(filename, lines):
    """Write lines back to file."""
    with open(filename, 'w') as f:
        for line in lines:
            if line != 'DELETEME':
                f.write(line)

def process_file(filename):
    """Read from file and manipulate lines."""
    with open(filename, 'r') as f:
        content = f.readlines()
    for i, line in enumerate(content):
        sys.stdout.write('{} {}'.format(i, line))
        # Exit conditions
        if line.startswith('=='):
            header = i - 1
            content = content[header:header+2] + ['\n'] + content[0:header] + content[header+3:]
            return finish(filename, content)
        if not line.strip():
            print 'blank line reached.'
        # Change metadata
        parts = line.split(':', 1)
        if len(parts) == 1:
            continue
        first = parts[0].strip()
        second = parts[1].strip()
        if first == 'public':
            content[i] = 'DELETEME'
            continue
        if first == 'language':
            content[i] = ':foobar: %s\n' % second
            continue
        elif first == 'tags':
            content[i] = ':tags: %s\n' % second[1:-1]
            continue
        elif first == 'summary':
            content[i] = ':' + content[i]
            continue
        elif first in ['tutorial', 'Doku', 'Ghana']:
            # These are articles starting with the mentioned words
            continue
        else:
            raise RuntimeError('Unknown meta key: ' + first)


if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('rst'):
                process_file('{}/{}'.format(root, f))
