def self_num():
    total = set(range(1,10001))
    not_self = set()

    for i in total:
        for j in str(i):
            i += int(j)
        not_self.add(i)

    self = sorted(total - not_self)

    for i in self:
        print(i)

self_num()