from twelvedays import counter_lines_writer, gifts_list_writer

def test_counter_lines_writer():
    assert counter_lines_writer(3) == "3rd"
    assert counter_lines_writer(4) == "4th"
    assert counter_lines_writer(11) == "11th"
    assert counter_lines_writer(12) == "12th"
    
def test_gifts_list_writer():
    assert gifts_list_writer(1) == ['A partridge in a pear tree.']
    assert gifts_list_writer(2) == ['Two turtle doves and',
                                         'A partridge in a pear tree.',
                                        ]
    assert gifts_list_writer(3) == ['Three french hens,',
                                         'Two turtle doves and',
                                         'A partridge in a pear tree.',
                                        ]
