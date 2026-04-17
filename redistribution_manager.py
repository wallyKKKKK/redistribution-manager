import argparse

class ProductRedistributionManager:
    def __init__(self):
        # Initialize storage for versions, releases, inventory, and locations
        self.versions = {}
        self.releases = {}
        self.inventory = {}
        self.locations = {}

    def manage_versions(self, version, action):
        '''Manage versions (add, remove, list).'''
        if action == 'add':
            self.versions[version] = "Version details..."
            print(f"Version {version} added.")
        elif action == 'remove':
            if version in self.versions:
                del self.versions[version]
                print(f"Version {version} removed.")
            else:
                print(f"Version {version} not found.")
        elif action == 'list':
            print("Current versions:", self.versions.keys())

    def manage_releases(self, release, action):
        '''Manage releases (add, remove, list).'''
        if action == 'add':
            self.releases[release] = "Release details..."
            print(f"Release {release} added.")
        elif action == 'remove':
            if release in self.releases:
                del self.releases[release]
                print(f"Release {release} removed.")
            else:
                print(f"Release {release} not found.")
        elif action == 'list':
            print("Current releases:", self.releases.keys())

    def manage_inventory(self, product, quantity, action):
        '''Manage inventory (add, remove, list).'''
        if action == 'add':
            self.inventory[product] = self.inventory.get(product, 0) + quantity
            print(f"Added {quantity} of {product}.")
        elif action == 'remove':
            if product in self.inventory and self.inventory[product] >= quantity:
                self.inventory[product] -= quantity
                print(f"Removed {quantity} of {product}.")
            else:
                print(f"Not enough inventory for {product}.")
        elif action == 'list':
            print("Current inventory:", self.inventory)

    def manage_locations(self, location, action):
        '''Manage locations (add, remove, list).'''
        if action == 'add':
            self.locations[location] = "Location details..."
            print(f"Location {location} added.")
        elif action == 'remove':
            if location in self.locations:
                del self.locations[location]
                print(f"Location {location} removed.")
            else:
                print(f"Location {location} not found.")
        elif action == 'list':
            print("Current locations:", self.locations.keys())

    def move_product(self, product, quantity, from_location, to_location):
        '''Move product from one location to another.'''
        if product in self.inventory and self.inventory[product] >= quantity:
            print(f"Moving {quantity} of {product} from {from_location} to {to_location}.")
            # Assuming simple move, you might want to implement more complex logic
        else:
            print(f"Not enough inventory of {product}.")

def main():
    parser = argparse.ArgumentParser(description='Product Redistribution Manager')
    subparsers = parser.add_subparsers(dest='command')

    # Versions command
    versions_parser = subparsers.add_parser('versions')
    versions_subparsers = versions_parser.add_subparsers(dest='action')
    versions_subparsers.add_parser('add', help='Add a new version')
    versions_subparsers.add_parser('remove', help='Remove a version')
    versions_subparsers.add_parser('list', help='List all versions')

    # Releases command
    releases_parser = subparsers.add_parser('releases')
    releases_subparsers = releases_parser.add_subparsers(dest='action')
    releases_subparsers.add_parser('add', help='Add a new release')
    releases_subparsers.add_parser('remove', help='Remove a release')
    releases_subparsers.add_parser('list', help='List all releases')

    # Inventory command
    inventory_parser = subparsers.add_parser('inventory')
    inventory_subparsers = inventory_parser.add_subparsers(dest='action')
    inventory_add_parser = inventory_subparsers.add_parser('add', help='Add product to inventory')
    inventory_add_parser.add_argument('product', type=str)
    inventory_add_parser.add_argument('quantity', type=int)
    inventory_remove_parser = inventory_subparsers.add_parser('remove', help='Remove product from inventory')
    inventory_remove_parser.add_argument('product', type=str)
    inventory_remove_parser.add_argument('quantity', type=int)
    inventory_subparsers.add_parser('list', help='List all inventory')

    # Locations command
    locations_parser = subparsers.add_parser('locations')
    locations_subparsers = locations_parser.add_subparsers(dest='action')
    locations_subparsers.add_parser('add', help='Add a new location')
    locations_subparsers.add_parser('remove', help='Remove a location')
    locations_subparsers.add_parser('list', help='List all locations')

    # Move command
    move_parser = subparsers.add_parser('move', help='Move product between locations')
    move_parser.add_argument('product', type=str)
    move_parser.add_argument('quantity', type=int)
    move_parser.add_argument('from_location', type=str)
    move_parser.add_argument('to_location', type=str)

    args = parser.parse_args()

    manager = ProductRedistributionManager()

    if args.command == 'versions':
        if args.action == 'add':
            manager.manage_versions('new_version', 'add')
        elif args.action == 'remove':
            manager.manage_versions('old_version', 'remove')
        elif args.action == 'list':
            manager.manage_versions(None, 'list')

    elif args.command == 'releases':
        if args.action == 'add':
            manager.manage_releases('new_release', 'add')
        elif args.action == 'remove':
            manager.manage_releases('old_release', 'remove')
        elif args.action == 'list':
            manager.manage_releases(None, 'list')

    elif args.command == 'inventory':
        if args.action == 'add':
            manager.manage_inventory(args.product, args.quantity, 'add')
        elif args.action == 'remove':
            manager.manage_inventory(args.product, args.quantity, 'remove')
        elif args.action == 'list':
            manager.manage_inventory(None, None, 'list')

    elif args.command == 'locations':
        if args.action == 'add':
            manager.manage_locations('new_location', 'add')
        elif args.action == 'remove':
            manager.manage_locations('old_location', 'remove')
        elif args.action == 'list':
            manager.manage_locations(None, 'list')

    elif args.command == 'move':
        manager.move_product(args.product, args.quantity, args.from_location, args.to_location)

if __name__ == "__main__":
    main()