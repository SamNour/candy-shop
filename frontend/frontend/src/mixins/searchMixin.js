export default {
  computed: {
    filteredBlogs: function () {
      return this.product.filter((product) => {
        return product.name.toLowerCase().match(this.search.toLowerCase());
      });
    },
  },
};
