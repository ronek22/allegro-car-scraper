﻿using AllegroREST.Models;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace AllegroREST
{
    class Program
    {

        static async Task Main()
        {
            AutoMapper.Mapper.Initialize(cfg => cfg.AddProfile<AutoMapperProfile>());
            await Run();
        }

        static async Task Run()
        {
            // configure dependencies
            var services = new ServiceCollection();
            services.AddHttpClient<AllegroClient>();
            var serviceProvider = services.BuildServiceProvider();

            // working with our client 
            var allegro = serviceProvider.GetRequiredService<AllegroClient>();
            await allegro.Authorize();
            
            await allegro.GetMotorOffers();
            //await allegro.RefreshAccessToken();
            //await allegro.GetMyOffers();
            //await allegro.GetListingByPhrase("motorola");
        }

    }
}
