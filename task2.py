from Stack import Stack

items = '[[{())}]'

if __name__ == '__main__':
    sequences_id = {'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
    sequences = Stack(items)
    buffer = Stack(sequences.pop()) 
    while not sequences.is_empty():
        check_sequence = sequences.pop()
        if buffer.is_empty():
            buffer.push(check_sequence)
            continue
        if (sequences_id[check_sequence] + sequences_id[buffer.peek()]) == 0:
            buffer.pop()
        else:
            buffer.push(check_sequence)

    if buffer.is_empty():
        print('Сбалансированно')
    else:
        print("Несбалансированно")
