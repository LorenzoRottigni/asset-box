class Asset:
    def __init__(self, blueprint):
        self.blueprint = blueprint
        asset = self.encode()
        for key, value in asset.items():
            setattr(self, key, value)
    
    @property
    def features(self):
        return self.__dict__.keys()
    
    @property
    def to_dict(self):
        dict = self.__dict__
        del dict['blueprint']
        return dict

    # def categorical(self):
    #     return [feature for feature in self.features if self.is_categorical(feature)]
    
    """
        Flats blueprint object into class attributes where each attribute name corresponds to the tree of keys of the blueprint object.
        Parameters:
          blueprint: dict
        Returns:
          Dict of attributes
    """
    def encode(self, blueprint=None):
        blueprint = blueprint or self.blueprint
        asset = {}
        for key, value in blueprint.items():
            if isinstance(value, dict):
                sub_blueprint = {f"{key}.{sub_key}": sub_value for sub_key, sub_value in self.encode(value).items()}
                asset.update(sub_blueprint)
            else:
                asset[key] = value
        
        return asset

    """
        Decodes class attributes into a blueprint object where each attribute name corresponds to the tree of keys of the blueprint object.
        Returns:
          Original blueprint object
    """
    def decode(self):
        blueprint = {}
        for attribute_name, attribute_value in vars(self).items():
            if attribute_name != 'blueprint':
                keys = attribute_name.split("_")
                current_dict = blueprint
                for key in keys[:-1]:
                    current_dict = current_dict.setdefault(key, {})
                current_dict[keys[-1]] = attribute_value
        return blueprint

