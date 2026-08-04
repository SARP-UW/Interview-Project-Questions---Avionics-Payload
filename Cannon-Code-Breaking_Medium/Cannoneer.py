from Cannon_Simulator import CannonSimulator
import buckets # Bucket maps and codes to try

# Constraints
VMIN = 5
VMAX = 15

# Selected code and map
bucket_map = buckets.BUCKET_MAP_A
code = buckets.CODE_A

# Find a solution to hitting each bucket in the playable area 
# If a code cannot be done, return a list of numbers that cannot
# be hit in the code 
def cannon_code_breaker(bucket_map: dict[str, tuple[float, float]],
                        code: str) -> list[str]:

    ## Your code goes here!
    
    return []

def main():
    
    # Fire in the hole
    out_of_range_buckets = cannon_code_breaker(bucket_map, code)
    
    if len(out_of_range_buckets) == 0:
        print("Some buckets could not be reached: ")
        for bucket in out_of_range_buckets:
            print(f"\t{bucket}")
    

if __name__ == "__main__":
    main()