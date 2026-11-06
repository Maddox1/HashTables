The two hash tables which used my bad hash function were abyssmal, especially the one which used linear probing.
This wasn't entirely due to the linear probing though, I just made my hash function way worse for it, which led to frankly ridiculous stats.

The rolling sum method for a hash function was the best I could find. It led to less collisions than the multiplicative and other various methods I tried.
That was why I used it for my final hash table, which attempted to combine the best of both worlds of linear probing and linked list hash tables.
While my final hash table did lead to (comparitavely) very few collisions, it did have quite a few unused buckets, and the time taken was also somewhat high.
With larger datasets, the time taken would probably get even worse, which means it probably isn't a great technique. Also, I had more unused buckets in my
final attempt than just standard linked list hashing, which is surprising to me.

In terms of time taken, linear probing seemed to be better, despite having far more collisions. This honestly could be due to me constantly recalculating
the hash function in my attempts for the linked list hash tables. I store the index as a variable for the linear probing attempts, and only had to recalculate
when there was a collision.

Bad hash function linked list: Lots of collisions and wasted memory, time taken actually somewhat low
Good hash function linked list: Few collisions, decent amount of unused buckets, time taken kinda high
Bad hash function linear probing: Millions of collisions, lots of wasted memory, time taken in the seconds.
Good hash function linear probing: Lots of collisions, but not a lot of unused memory, and time taken is low (similar to bad linked, but better in every metric)
Final hash linear+linked: Very few collisions, but a good amount of wasted memory, time taken is in between good linked and good linear