from ezbot.process import process_request


def drive(debug=False):
    print('Hello.')
    action = None
    while action != 'DONE':
        action, response, tokens = process_request(input('What? '), False)
        print(response)
        if debug:
            print(tokens, action)


if __name__ == '__main__':
    drive()
