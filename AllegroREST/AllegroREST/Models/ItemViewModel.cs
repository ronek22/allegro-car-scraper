using System;

namespace AllegroREST.Models
{
    [Serializable]
    public class ItemViewModel {
        private ItemViewModel() {}

        public string Name {get; set;}        
        public string OfferId { get; set; }
        public decimal Price { get; set; }
    }
}