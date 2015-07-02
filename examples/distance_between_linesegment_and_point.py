__author__ = 'Jonas I Liechti'
from vecpy import Vector as Vec


# How to get the distance between a segment and a point
def point2segment_dist(point, segment):
    """
    Return the distance between a segment of a line and a point

    :param point:
    :param segment:
    :return:
    """
    sp_vec = Vec(segment[0], point)  # create a vector from start of the segment to the point
    seg_vec = Vec(segment)  # create a vector along the segment
    proj_scale = seg_vec.proj(sp_vec, True)  # project the sp_vector to the segment vector and get the ration of the
    # length of those two parallel vectors
    if proj_scale <= 0:  # if the projection has not the same direction
        dist = sp_vec.length
    elif proj_scale >= 1:  # if the projection is longer than the segment vector
        dist = Vec(segment[1], point).length
    else:  # get the length from the part of sg_vec orthogonal to the segment vector
        ortho_v = seg_vec.proj(sp_vec) - sp_vec
        dist = ortho_v.length
    return dist

# line segment:
x = [4, 5]
y = [1, 1]
my_seg = (x, y)
# a point:
p = [-1, -2]
print point2segment_dist(p, my_seg)