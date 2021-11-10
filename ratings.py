"""Restaurant rating lister."""

Rest = {
    'Florean Fortescues Ice Cream Parlour is rated at' : 4,
    'Jellied Eel Shop' : 3,
    'The Tavern' : 3,
    'Luchino Caffe' : 1,
    'The Porcupine' : 5,
    'Diagon Alley cafe' : 2,
    'The Bear & Staff' : 2,
    'Ministry Munchies' : 1,
    'Chip Shop' : 3,
    'Eternelles Elixir of Refreshment' : 5,
    'Big Bean Shack' : 3,
    'The Club' : 2

}


# put your code here
r = input('Please enter a Resaurant ')
s = input('Please assign it a score ')
Rest.update({r : s})
print(Rest)