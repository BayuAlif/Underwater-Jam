# NOTE: MC's sprite is put on the "mc_front" layer (above the dialogue box) by
# config.tag_layer in assets.rpy. Do NOT add show_layer here - that moves
# MC's *dialogue box* onto the same layer, which covers the MC sprite again.
define mc = Character("Mc", color="#ffffff", image="mc")
