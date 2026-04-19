#Test the ability to define simple facts and one-step inferences

# Create a knowledge base for a "Smart Warehouse" system.
#Define facts for three items and their storage requirements (e.g., requires(item1, cold_storage)., requires(item2, ambient).).
knowledge_base = {
    'item1': 'cold_storage',
    'item2': 'ambient',
    'item3': 'cold_storage'
}
#Define a rule needs_refrigeration(Item) that is true if the item requires cold_storage.
def needs_refrigeration(item):
    return knowledge_base.get(item) == 'cold_storage'  
#Write the query to list all items that need to be kept in the freezer.
items_needing_refrigeration = [item for item in knowledge_base if needs_refrigeration(item)]
print("Items that need refrigeration:", items_needing_refrigeration)
