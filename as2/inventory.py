'''
Daniel Sawyer Assignment 2 inventory Fall 2017
'''
def displayInventory(inventory):
	print('Inventory:')
	sum = 0
	for i, j in inventory.items():
		print(j, i)
		sum += j
	print('Total number of items: ' + str(sum))

def addToInventory(inventory, addedItems):
	for i in addedItems:
		if i not in inventory:
			inventory[i] = 1
		else:
			inventory[i] += 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)