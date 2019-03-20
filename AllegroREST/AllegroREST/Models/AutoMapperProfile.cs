using System.Collections.Generic;
using AutoMapper;

namespace AllegroREST.Models
{
    public class AutoMapperProfile : Profile
    {
        public AutoMapperProfile()
        {
            CreateMap<Item, ItemViewModel>()
                .ForMember(dest => dest.OfferId, opt => opt.MapFrom(s => s.Id))
                .ForMember(dest => dest.Price, opt => opt.MapFrom(s => s.SellingMode.Price.Value))
                .ForMember(dest => dest.Name, opt => opt.MapFrom(s => s.Name));
        }
    }
}