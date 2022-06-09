class Poste_hta_bt(codification,name=''):
    """ Class Poste HTA/BT"""
    def __init__(self, *args, **kwargs):
        pass

    def create_empty_network(name="", f_hz=50., sn_mva=1, add_stdtypes=True):
        """
        This function initializes the pandapower datastructure.

        OPTIONAL:
            **f_hz** (float, 50.) - power system frequency in hertz

            **name** (string, None) - name for the network

            **sn_mva** (float, 1e3) - reference apparent power for per unit system

            **add_stdtypes** (boolean, True) - Includes standard types to net

        OUTPUT:
            **net** (attrdict) - PANDAPOWER attrdict with empty tables:

        EXAMPLE:
            net = create_empty_network()

        """
        net = pandapowerNet({
            # structure data
            "bus": [('name', dtype(object)),
                    ('vn_kv', 'f8'),
                    ('type', dtype(object)),
                    ('zone', dtype(object)),
                    ('in_service', 'bool'), ],
            "load": [("name", dtype(object)),
                     ("bus", "u4"),
                     ("p_mw", "f8"),
                     ("q_mvar", "f8"),
                     ("const_z_percent", "f8"),
                     ("const_i_percent", "f8"),
                     ("sn_mva", "f8"),
                     ("scaling", "f8"),
                     ("in_service", 'bool'),
                     ("type", dtype(object))],
            "sgen": [("name", dtype(object)),
                     ("bus", "i8"),
                     ("p_mw", "f8"),
                     ("q_mvar", "f8"),
                     ("sn_mva", "f8"),
                     ("scaling", "f8"),
                     ("in_service", 'bool'),
                     ("type", dtype(object)),
                     ("current_source", "bool")],
            "motor": [("name", dtype(object)),
                      ("bus", "i8"),
                      ("pn_mech_mw", "f8"),
                      ("loading_percent", "f8"),
                      ("cos_phi", "f8"),
                      ("cos_phi_n", "f8"),
                      ("efficiency_percent", "f8"),
                      ("efficiency_n_percent", "f8"),
                      ("lrc_pu", "f8"),
                      ("vn_kv", "f8"),
                      ("scaling", "f8"),
                      ("in_service", 'bool'),
                      ("rx", 'f8')
                      ],

        })