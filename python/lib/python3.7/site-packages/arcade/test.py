import numpy as np

array_of_positions = [[1, 2], [3, 4]]
array_of_angles = [5, 6]

buffer_type = np.dtype([('position', '2f4'), ('angle', 'f4')])
sprite_data = np.zeros(len(array_of_angles), dtype=buffer_type)
sprite_data['position'] = array_of_positions
sprite_data['angle'] = array_of_angles

print(sprite_data)
my_bytes = sprite_data.tobytes()
for my_byte in my_bytes:
    print(f"{my_byte:02x}", end=" ")

