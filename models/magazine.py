class Magazine:
      def __init__(self, id, name, category="general"):
          self._id = id
          self.name = name
          self._category = category 
      @property
      def id (self):
          return self._id
      @property
      def name(self):
          return self._name
      @name.setter
      def name(self, value):
          if not isinstance(value, str):
              raise TypeError("Name must be a string.")
          if not (2 <= len(value) <= 16):
              raise ValueError("Name must be between 2 and 16 characters.")
          self._name = value
      @property
      def category(self):
          return self._category

      @category.setter
      def category(self, value):
          if not isinstance(value, str):
              raise TypeError("Category must be a string.")
          if len(value) <= 0:
              raise ValueError("Category must be longer than 0 characters.")
          self._category = value


      def __repr__(self):
          return f'<Magazine {self.name}>'
