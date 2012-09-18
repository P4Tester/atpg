'''
    <Run reachability test using NuSMV>
    Copyright (C) 2012  Stanford University

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Created on Jan 4, 2012

@author: Peyman Kazemian
'''
from utils.load_stanford_backbone import *
from headerspace.nu_smv_generator import *
from time import time

(port_map,port_reverse_map) = load_stanford_backbone_port_to_id_map()
src_port_id = port_map["bbra_rtr"]["te6/3"]
dst_port_id = port_map["roza_rtr"]["te3/3"]+20000
via_ports = [port_map["bbrb_rtr"]["te6/3"],port_map["bbrb_rtr"]["te6/3"]+20000]
nusmv = load_tf_to_nusmv()
st = time()
#print nusmv.run_nusmv_one_path_via_ports_reachability(src_port_id, dst_port_id,via_ports)
print nusmv.run_nusmv_reachability(src_port_id, dst_port_id)
en = time()
print en-st