from table import Table


#create a class `Openspace`
class Openspace:
    #- `number_of_tables` which is an integer and tables is a list
    def __init__(self, number_of_tables:int = 6):
        self.number_of_tables = number_of_tables
        self.tables = []
        for i in range(number_of_tables):
            self.tables.append(Table())      
    

    def organize(self, tables):
        index = 0
        for table in self.tables:
            for seat in tables[index]:
                if index < len(tables):
                    table.add_seat(seat)
            index += 1

        return self.tables
    
    #return the number of free seats in the openspace
    def get_number_of_free_seats(self):
        free_seats = 0
        for table in self.tables:
            free_seats += table.left_capacity()
        return free_seats
    
    #return the number of occupied seats in the openspace
    def get_number_of_occupied_seats(self):
        occupied_seats = 0
        for table in self.tables:
            occupied_seats += table.capacity - table.left_capacity()
        return occupied_seats
    
    #return the number of people in the openspace
    def get_number_of_people(self):
        return self.get_number_of_occupied_seats()
    
    #return the number of tables with free spots
    def get_number_of_tables_with_free_spots(self):
        count = 0
        for table in self.tables:
            if table.has_free_spot():
                count += 1
        return count
    
    #return the number of tables with no free spots
    def get_number_of_tables_with_no_free_spots(self):
        count = 0
        for table in self.tables:
            if not table.has_free_spot():
                count += 1
        return count
    
    
    #display the different tables and there occupants in a nice and readable way
    def display(self):
        for table in self.tables:
            table.display()
        return self.tables