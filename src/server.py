from flask import Flask
app=Flask('__main__')

@app.route('/test_2')

def test_2():
    return 'this is test 2'
@app.route('/')
def test():
    return 'Hello world'

def main():
   app.run()

if __name__=='__main__':
    main()
