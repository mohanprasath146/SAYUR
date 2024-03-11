class ParkingSlot():
    def __init__(self):
        self.N = 3
        self.X = 3
        self.total_slots = self.N*self.X
        self.park_data = [("", "") for i in range(self.total_slots)]
        self.booked = 0

    #parking space allotment
    def park(self, reg_no, color):
        if self.booked < self.total_slots:
            tup = ()
            ind = self.park_data.index(("", ""))
            self.park_data[ind] = (reg_no, color)
            print(f"Vehicle is parked at {ind}.")
            self.booked += 1
        else:
            print("Parking full.")

    def unpark(self, reg_no):
        out = [slot for slot in self.park_data if slot[0]==reg_no]
        
        if out:
            self.booked -= 1
        self.park_data.remove(out[0])

    def fetch_slot_by_reg(self, reg_no):
        out = [slot for slot in self.park_data if slot[0]==reg_no]
        print(f"Parking slot for {reg_no}:{out}")

    def fetch_slot_by_col(self, col):
        out = [slot for slot in self.park_data if slot[1]==col]
        print(f"Parking slot of all the cars of color {col}:{out}")

    def prnt(self):
        print(f"\n{self.park_data}")


if __name__ == "__main__":
    obj_park = ParkingSlot()
    obj_park.park("Reg1", "White")
    obj_park.prnt()
    obj_park.park("Reg2", "Red")
    obj_park.prnt()
    obj_park.park("Reg3", "Blue")
    obj_park.prnt()
    obj_park.unpark("Reg2")
    obj_park.prnt()
    obj_park.fetch_slot_by_reg("Reg1")
    obj_park.prnt()
    obj_park.fetch_slot_by_col("Blue")